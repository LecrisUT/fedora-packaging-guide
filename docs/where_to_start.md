# Where do I begin?

Fedora/RPMs build process is all contained in a spec-file (file with the suffix
`.spec`).

## Where do I find these spec-files?

Depending on the projects you are interested in, you can find spec-files under:

::::{tab-set}

:::{tab-item} Fedora source

Fedora sources are found in [src.fedoraproject.org], under `rpms/*`, for
example [rpms/bash].

```{hint} Trouble finding the link?
Sometimes the _source_ spec/rpm (what is in the src.fedoraproject.org) is
differently named to the _binary_ rpms (what you install with `dnf install`).

You can find the original source from `dnf info` or something like [pkgs.org].
```

```{todo}
Screenshot of src.fp.o
```

[src.fedoraproject.org]: https://src.fedoraproject.org
[rpms/bash]: https://src.fedoraproject.org/rpms/bash
[pkgs.org]: https://pkgs.org
:::

:::{tab-item} Copr project

A single copr project can build multiple packages, which in turn can have
multiple builds (updates) for multiple chroots (distro bases), which in turn
ultimately provide the rpms.

What you need to navigate to here is a build which you want to investigate.

```{todo}
Screenshot of copr build
```
:::

:::{tab-item} Upstream

Upstream projects can also have their own spec file. One thing to be conscious
about though is whether the project's sources are alongside the spec file or
not. The latter case is called a dist-git, the same as with "Fedora source".

```{todo}
Screenshot of upstream project
```

```{note}
Building rpms with upstream sources is a more involved process requiring quite
some automation. This will be covered in section [][upstream]
```
[upstream]: upstream.md
:::

::::
