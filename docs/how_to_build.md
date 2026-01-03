# Ok, so how do I start building already?

Now that you know how to read the spec file (in excruciating detail?) and know
what to expect during the build, let's try to actually build one of those
packages. The starting point here is just a folder with the spec file and all
its sources and patches.

```{tip}
To get the sources defined externally run `spectool -g *.spec`.
```

::::{tab-set}

:::{tab-item} fedpkg
:sync: fedpkg

_After making sure you do not have a `sources` file present next to the spec
file_, the build process using `fedpkg` is quite straightforward, simply run
```console
$ fedpkg mockbuild
```
:::

:::{tab-item} mock
:sync: mock

If you do not want to use any helper scripts to do the building for you, you
can invoke the `mock` build directly from an `srpm`, i.e. the source rpm,
basically just an archive of the spec file and its sources and patches. First
to get the `srpm` you can use `fedpkg srpm` or `mock --buildsrpm` [^1]
```console
$ mock --buildsrpm --spec *.spec --sources ./ --resultdir results
$ mock ./results/*.src.rpm
```
:::

:::{tab-item} packit
:sync: packit

If you start from a project that has packit integration you can build the
project locally using
```console
$ packit build in-mock
```

How and why one would setup a packit integration is covered in the [automation]
section.
:::

:::{tab-item} rpmbuild

**Please don't**. Although this is the bare core that is used underneath
`mock`, this approach has too many hidden failures and dependencies, e.g. it
uses whatever packages and files you have locally.
:::

::::

## What should I look out for?

Regardless of how you triggerred the build, you should find the results
containing logs (mainly `build.log` and `root.log`) regardless if it succeeded
or failed, and the `.rpm` artifacts only if it was successful.

You might encounter numerous failures that you should have some basic knowledge
of the build system in order to be able to debug. For some of the common build
failures, please check the [build FAQ].

[^1]: You could also get the srpm from a known package with
`dnf download --srpm` or from some other sources you might have encountered in
the [where to start] section.

## I need to build multiple packages depending on each other

Wow you are quite ahead of the curve :). The workflows for building multiple
packages is much more limited and primarily found in the [automation] section.
For building locally you have a few options

::::{tab-set}

:::{tab-item} fedpkg
:sync: fedpkg

The official support for multi-package build here is using `chain-build`, but
that requires already [being a packager] and knowing how to build with `koji`,
which is out of scope here. Another option is to do the builds manually one
after another and reusing the rpm files
```console
$ fedpkg mockbuild --extra-pkgs results/*.rpm
```
:::

:::{tab-item} mock
:sync: mock

After building all the srpm manually you can do a chain build them using
`--chain`
```console
$ mock --chain /path/to/first.src.rpm /path/to/second.src.rpm
```
:::

::::

[automation]: automation.md
[being a packager]: becoming_packager.md
[build FAQ]: build_faq/index.md#my-build-failed
[where to start]: where_to_start.md
