# Why should I even bother packaging for Fedora?

Packaging to Linux distributions will help both your project and the ecosystem
in general.

## As a user

Even as a user of a particular project you can get involved.

### You are probably an early explorer of the project

If something is not packaged in a distro it is likely someone else did not have
your same set of interests or found the project. You might be an early pioneer
and at some point someone has to do the work of distributing the project and
sharing it more broadly. That could be you.

If packaging seems too big of a commitment, you can still help by letting
others know about your interest in one of the various Fedora channels [^1].
Worst case scenario, people are just too busy with maintaining other packages,
but what they will always offer is guidance for how you can do the work
yourself.

[^1]: [#fedora], [#join], or other rooms in [#fedora-space]

[#fedora]: https://matrix.to/#/#fedora:fedoraproject.org
[#join]: https://matrix.to/#/#join:fedoraproject.org
[#fedora-space]: https://matrix.to/#/#fedora-space:fedoraproject.org

#### You do not need to be a developer to be a packager

To be a packager you do not need in depth knowledge of a project, its
surrounding ecosystem or sometimes even the programming language it uses.
Basic knowledge of how to install, and run the project is all that is required
technically to be packager. Surprisingly what you need more are people skills
to communicate with the upstream and fellow packagers.

### `curl ... | bash` is a security nightmare

Probably as a user this is how you were introduced to install a project. But
have you checked what it is actually doing? Does it not do something fishy?
As a packager you are vetting that a project is what it claims to be, and it
is working properly. Other users would then not have to analyze the project.

### A package is too old or has trouble keeping up

This often happens because of the lack of time of the main packager. This is
where you can help, either by helping with the updates, or just letting the
packager know that there are users out there who care and are waiting for this.

## As a developer

Packaging to Fedora will help both your project and the ecosystem in general.

### Dependency testing

One core part of Linux distributions is making sure things work together. There
is extensive testing and automation in Fedora that catch issues as early as
possible.

#### But I do not want to test unstable beta versions

This is just kicking the can down the road, where any breakage in the
dependency is more your problem then theirs. Many bugs and issues are caught
early when a package updates, before it gets to affect you or your users. At
that point you get a stronger voice and influence regarding breaking changes.

#### You get help from the packager

Often times when there is a dependency issue, a packager would catch it in a
different package, and would offer to help you with a patch.

### You get reverse dependency checks

If you are a library project, it is often hard to figure out how your changes
will impact other projects. But if those projects are also packaged in Fedora,
you effectively get a reverse dependency testing. And the tools are getting
better and better to make this available close to your development cycle.

### Knowing the status of the ecosystem

Packagers would often know about the state of various projects, which ones
are no longer maintained, what alternatives can be used, new projects that
try to do the same thing as you do, etc. If something is relevant they will
contact you for your opinions.
