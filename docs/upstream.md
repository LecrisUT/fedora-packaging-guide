# Packaging seems like a big commitment, can I just do this just for myself?

Yes, you can build and distribute rpm-based packages for your own purpose and
desires, and we will go through some ways of doing that here. But you should
consider what packaging to Fedora brings:
- Periodic rebuilds (at least twice a year) with the most recent packages on
  Fedora.
- Discoverability and contributions within Fedora and its derivatives.
- Extensive testing infrastructure, including some reverse-dependency testing
  by the packagers of a dependency you use.
- Helping community that can sometimes help you maintain a package.

You would generally lose these if you publish your packages on your own managed
repository. But many Fedora packages are also managed externally in addition to
the packaging done on Fedora, from which you can take some inspiration.

## Upstream packaging

Packit offers integration for upstream projects to run the equivalent build
system from Fedora on the git forge that the upstream uses for development.
This was primarily covered in the [Packit automation] section, see it for more
details. The only difference here is that now the `.packit.yaml` configuration
is much simpler since Packit is built to support this out of the box.
```yaml
specfile_path: my-package.spec

targets:
  - fedora-rawhide

jobs:
  - job: copr_build
    trigger: commit
```
Packit will take a git archive of the current repo and use it as the `Source0`
in the spec file.

## Persistent copr project

```{warning}
The projects on copr are not regularly rebuilt, so a build that succeeded at
some point may not be able to rebuild or be installable later on.
```

Beyond the usage for development work, copr can also be used to hosted
persistent repositories for users to use. For this you simply need to create a
copr project and hook it to your desired automation. For the
[Packit automation] this involves setting `owner` and `project` for the
`copr_build` job
```yaml
jobs:
  - job: copr_build
    trigger: commit
    owner: lecris
    project: atuin
```
granting builder privilege to Packit
```console
$ copr edit-permissions --builder packit lecris/atuin
```
and configuring the copr project for the Packit integration

```{image} images/upstream/copr_0.png
```

[Packit automation]: automation.md#packit-automation
