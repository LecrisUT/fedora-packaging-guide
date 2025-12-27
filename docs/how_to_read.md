# How do I read this magical "spec-file"?

Let's start with a minimal example spec file. Here you can see a few examples
depending on the build-system/tools used during the packaging.

:::::{tab-set}

::::{tab-item} cmake
:sync: cmake

:::{toggle}
```{literalinclude} examples/span.spec
:language: spec
```
:::
::::

::::{tab-item} python
:sync: python

:::{toggle}
```{literalinclude} examples/python-pytest-check.spec
:language: spec
```
:::
::::

:::::

## Step1: What is being done?

The main parts of the spec file are the build process steps which are separated
into various sections:

`%prep`
: Prepare (extract) the sources and

`%generate_buildrequires`
: Add additional `BuildRequires` dynamically (more on that later)

`%conf`
: Run `configure` or equivalents

`%build`
: Do the main build steps of the project

`%install`
: Install all files in a staging location as they will be seen after you
  `dnf install` the package

`%check`
: Run available tests preferably against the staged files

The sections are executed in that order, and can be omitted.

Let's look at the minimal example and decompose what's happening:

::::{tab-set}

:::{tab-item} cmake
:sync: cmake

```{literalinclude} examples/span.spec
:language: spec
:lines: 44-61
```

`%prep`
: Extract the source defined in `Source`, apply any patches defined by `Patch`,
  and `cd` into the folder inside the archive defined by `-n` option.
: (Common across all build systems)

`%conf`
: Run a `cmake` (configure) step with any relevant `-D` options

`%build`
: Run the `cmake --build` step

`%install`
: Run `cmake --install`

`%check`
: Run the provided `ctest` (in the build directory)

:::

:::{tab-item} python
:sync: python

```{literalinclude} examples/python-pytest-check.spec
:language: spec
:lines: 23-41
```

`%prep`
: Extract the source defined in `Source`, apply any patches defined by `Patch`,
  and `cd` into the folder inside the archive defined by `-n` option.
: (Common across all build systems)

`%pyproject_buildrequires`
: Get all `build-system.requires`, `project.requires` from `pyproject.toml` and
  add them to the current `BuildRequires`

`%build`
: Run `pip wheel`

`%install`
: Install the built wheel
: Save the installed file list under `%{pyproject_files}`

`%check`
: Run `pytest`

:::

::::


## Step0: Wait, where are the sources coming from?

Ok, I've lied, the most important thing you should be interested in as a
packager is the metadata sections which, among many other things, defines what
are the sources (and patches) currently used. Otherwise, there is little
variance between the actual build instructions of each package.

::::{tab-set}

:::{tab-item} cmake
:sync: cmake
```{literalinclude} examples/span.spec
:language: spec
:lines: 4-21
:emphasize-lines: 9,12,14
```
:::

:::{tab-item} python
:sync: python
```{literalinclude} examples/python-pytest-check.spec
:language: spec
:lines: 1-11
:emphasize-lines: 8
```
:::

::::

These `Source` and `Patch` lines can point to an external url that would be
downloaded or a local file present next to the spec file.

```{tip}
Use `spectool -g *.spec` to download all of the sources defined in the spec
file
```

## Step2: Dependencies

Of course the sources and instructions are not sufficient to build the package,
you also need the build-time and runtime dependencies of the current package.


::::{tab-set}

:::{tab-item} cmake
:sync: cmake
```{literalinclude} examples/span.spec
:language: spec
:lines: 4-21
:emphasize-lines: 16-18
```
:::

:::{tab-item} python
:sync: python
```{literalinclude} examples/python-pytest-check.spec
:language: spec
:lines: 1-11
:emphasize-lines: 11
```
:::

::::

These are defined with the `BuildRequires` and `Requires` fields. Of course
managing these fields manually would be very time-consuming, so often these are
kept to the bare minimum needed. The real dependencies are often defined
dynamically either from the source files for the `BuildRequires` using
`%generate_buildrequires` or from the installed files for the `Requires` which
are handled behind the scenes (e.g. the dependencies on the libraries is never
defined manually instead these are extracted from the binary/library files).

## Step3: `%files` and `%package` sections

After you've installed the files, you also need to define the expected files
and their locations to be packaged, which is defined in the `%files` section.

However, often you would want to separate where the files are located, e.g. the
development files being in a `*-devel` sub-package, the documentations in a
`*-docs` sub-package, etc. This is done by defining various `%package` sections
sharing the same metadata fields as the top level/source package.

::::{tab-set}

:::{tab-item} cmake
:sync: cmake
```{literalinclude} examples/span.spec
:language: spec
:lines: 34-41,62-68
```
:::

:::{tab-item} python
:sync: python
```{literalinclude} examples/python-pytest-check.spec
:language: spec
:lines: 18-20,42-46
```
:::

::::

## Step4: Macros

As you've already seen throughout the files, the spec file is riddled with
macros which you can find as either `%{macro_name}` or `%macro_name`. These
simplify the repetition of various parts of the spec file. Some of these are
pre-defined from corresponding fields such as `%version` or `%url`, defined in
some commonly sourced `/usr/lib/rpm/macros.d/macros.*` file such as for the
`%cmake`, `%pyproject_wheel` etc., or they can be defined/overriden directly in
the spec file with `%global` or equivalents.


::::{tab-set}

:::{tab-item} cmake
:sync: cmake
```{literalinclude} examples/span.spec
:language: spec
:lines: 1-32
:emphasize-lines: 1,2,23-30
```
:::

:::{tab-item} python
:sync: python
```{literalinclude} examples/python-pytest-check.spec
:language: spec
:lines: 1-16
:emphasize-lines: 13-14
```
:::

::::

## Step5: Control parameters

Sometimes you will find a spec file defining `%bcond` fields which are
basically just control fields to turn on/off a process during the build with
the `%if` and `%with_*`/`%without_*` macros. More on how to actually invoke
them in the [how to build] section of this guide.

[how to build]: ./how_to_build.md

## Step6: The rest

As you can see not all fields are documented here as this is beyond the scope
of this guide. Some of the fields usage is straightforward. Other times the
fields usage have quite a bit of nuance attached to it which is best explored
with a fellow Fedora packager, most of which being in the Fedora [#devel] room.

[#devel]: https://matrix.to/#/#devel:fedoraproject.org
