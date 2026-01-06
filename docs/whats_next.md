# I got the gist of it, is that all?

Congratulations on making through this guide. Here are some tips on how to
level up your packaging.

## Participate in change proposals

Big (and medium) changes are proposed and discussed on Fedora through the
[Change proposals]. If you are subscribed to the [devel mailing list], you will
be informed of these changes as soon as they are published. Anyone is welcome
to participate in the discussions, and it helps steer Fedora in a direction you
desire.

## Participate in the discussions in the devel and sig rooms

Fedora packaging is driven by the community and everyone is welcome to join it.
The general community is in the [#devel] room, but there are additional sig
rooms that you can find in the [#fedora-space] or ask around in the [#join] or
[#devel] rooms.

Some things you can expect there:
- discussions on current problems and proposes
- tips and help on packaging, including some new features recently developed
- upstream issues and how to report/address them
- general nerdery

## Design additional tests

The `%check` section in the spec file is often very restrictive, e.g. not being
able to access internet or preparing complicated setups, and is primarily used
to run the tests defined by the upstream projects. If you want more advanced
tests, you should look into writing some tests using [tmt]. To get started you
just need to write a plan (the environment where tests are run) and some tests,
for example, a minimum setup can look like
```console
$ tmt init
$ cat plans.fmf
exectue:
  how: tmt
$ cat tests.fmf
# As part of the tests we assume we have a package named `hello` that we want
# to install as part of the tests
require:
  - hello

/smoke:
  summary: A minimal smoke test
  description: |
    The purpose of this test is just to illustrate how to define a simple tmt
    test. The test simply tries to run the `hello` executable and checks that
    it did not fail to do so.
  test: hello
$ tree -a .
.
├── .fmf
│   └── version
├── hello.spec
├── plans.fmf
└── tests.fmf
```

If the package is on Fedora or has Packit integration, the tmt tests are
executed as part of the pull request CI. You can also execute these tests
locally using
```console
$ tmt run -a \
  provision --how=container --image=rawhide
```
This tells tmt to use the plans and tests defined in the `.fmf` files, but on
top of that overwrite/append some steps. In this case it says to `provision` a
Fedora rawhide container and run the tests under that.

```{todo}
Add instructions using artifact interface
```

[#devel]: https://matrix.to/#/#devel:fedoraproject.org
[#fedora-space]: https://matrix.to/#/#fedora-space:fedoraproject.org
[#join]: https://matrix.to/#/#join:fedoraproject.org
[Change proposals]: https://discussion.fedoraproject.org/c/project/changes/89
[devel mailing list]: https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/
[tmt]: https://tmt.readthedocs.io/en/stable/index.html
