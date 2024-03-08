%global debug_package %{nil}

%bcond_with bootstrap2

# Run tests in check section
%bcond_with check

# https://github.com/golang/tools
%global goipath		golang.org/x/tools
%global forgeurl	https://github.com/golang/tools
Version:		0.17.0

%gometa

%global auth_commands authtest cookieauth gitauth netrcauth
%global commands benchcmp bundle callgraph compilebench digraph eg file2fuzz fiximports getgo go-contrib-init godex godoc goimports gomvpkg gorename gotype goyacc guru html2article present splitdwarf ssadump stress stringer toolstash

Summary:	Various packages and tools that support the Go programming language
Name:		golang-x-tools

Release:	1
Source0:	https://github.com/golang/tools/archive/v%{version}/tools-%{version}.tar.gz
%if %{with bootstrap2}
# Generated from Source100
Source3:	vendor.tar.zst
Source100:	golang-package-dependencies.sh
%endif
# (debian)
Patch0:		0013-Disable-telemetry-in-gopls.patch
URL:		https://github.com/golang/tools
License:	BSD
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
%if ! %{with bootstrap2}
BuildRequires:	golang(github.com/google/go-cmp/cmp)
BuildRequires:	golang(github.com/jba/printsrc)
BuildRequires:	golang(github.com/yuin/goldmark)
BuildRequires:	golang(github.com/yuin/goldmark/ast)
BuildRequires:	golang(github.com/yuin/goldmark/parser)
BuildRequires:	golang(github.com/yuin/goldmark/renderer/html)
BuildRequires:	golang(github.com/yuin/goldmark/text)
BuildRequires:	golang(golang.org/x/mod/modfile)
BuildRequires:	golang(golang.org/x/mod/module)
BuildRequires:	golang(golang.org/x/mod/semver)
BuildRequires:	golang(golang.org/x/net/html)
BuildRequires:	golang(golang.org/x/net/html/atom)
BuildRequires:	golang(golang.org/x/net/websocket)
BuildRequires:	golang(golang.org/x/sync/errgroup)
BuildRequires:	golang(golang.org/x/text/unicode/runenames)
BuildRequires:	golang(golang.org/x/vuln/scan)
BuildRequires:	golang(gopkg.in/yaml.v3)
BuildRequires:	golang(honnef.co/go/tools/analysis/lint)
BuildRequires:	golang(honnef.co/go/tools/quickfix)
BuildRequires:	golang(honnef.co/go/tools/simple)
BuildRequires:	golang(honnef.co/go/tools/staticcheck)
BuildRequires:	golang(honnef.co/go/tools/stylecheck)
BuildRequires:	golang(mvdan.cc/gofumpt/format)
BuildRequires:	golang(mvdan.cc/xurls/v2)
%endif

%description
This package provides the golang.org/x/tools module,
comprising various tools and packages mostly for static
analysis of Go programs.

%if ! %{with bootstrap2}
It also contains the golang.org/x/tools/gopls module, whose
root package is a language-server protocol (LSP) server for
Go. An LSP server analyses the source code of a project and
responds to requests from a wide range of editors such as
VSCode and Vim, allowing them to support IDE-like functionality.
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/*

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc README.md

#-----------------------------------------------------------------------

%package -n golang-godoc
Summary:        Documentation tool for the Go programming language
Epoch:          1
Obsoletes:      golang-godoc = 1.1.2

%description -n golang-godoc
Godoc extracts and generates documentation for Go programs.

%files -n golang-godoc
%license LICENSE
%doc README.md
%{_bindir}/godoc

#-----------------------------------------------------------------------

%package -n golang-gotype
Summary:        Go programming language source code analysis tool

%description -n golang-gotype
The gotype command, like the front-end of a Go compiler, parses and type-checks
a single Go package. Errors are reported if the analysis fails; otherwise
gotype is quiet (unless -v is set).

%files -n golang-gotype
%license LICENSE
%doc README.md
%{_bindir}/gotype

#-----------------------------------------------------------------------

%package -n golang-html2article
Summary:        Tool for creating articles from HTML files

%description -n golang-html2article
This program takes an HTML file and outputs a corresponding article file
in present format. See: golang.org/x/tools/present

%files -n golang-html2article
%license LICENSE
%doc README.md
%{_bindir}/html2article

#-----------------------------------------------------------------------

%package        auth
Summary:        Tools implementing the GOAUTH protocol

%description    auth
%{summary}.

%files    auth
%license LICENSE
%doc README.md
%{_bindir}/authtest
%{_bindir}/cookieauth
%{_bindir}/gitauth
%{_bindir}/netrcauth

#-----------------------------------------------------------------------

%package        callgraph
Summary:        Tool for reporting the call graph of a Go program

%description    callgraph
%{summary}.

%files    callgraph
%license LICENSE
%doc README.md
%{_bindir}/callgraph

#-----------------------------------------------------------------------

%package        compilebench
Summary:        Benchmarks the speed of the Go compiler

%description    compilebench
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/compilebench for more information.

%files    compilebench
%license LICENSE
%doc README.md
%{_bindir}/compilebench

#-----------------------------------------------------------------------

%package        digraph
Summary:        Tool for queries over unlabelled directed graphs in text form

%description    digraph
The digraph command performs queries over unlabelled directed graphs
represented in text form.

%files    digraph
%license LICENSE
%doc README.md
%{_bindir}/digraph

#-----------------------------------------------------------------------

%package        gorename
Summary:        Tool for precise type-safe renaming of identifiers in Go code

%description    gorename
The gorename command performs precise type-safe renaming of identifiers in Go
source code.

%files    gorename
%license LICENSE
%doc README.md
%{_bindir}/gorename

#-----------------------------------------------------------------------

%package        stringer
Summary:        Tool to automate creating methods satisfying the fmt.Stringer interface

%description    stringer
Stringer is a tool to automate the creation of methods that satisfy the
fmt.Stringer interface.

%files    stringer
%license LICENSE
%doc README.md
%{_bindir}/stringer

#-----------------------------------------------------------------------

%package        godex
Summary:        Tool to dump exported information for Go packages or objects

%description    godex
The godex command prints (dumps) exported information of packages or selected
package objects.

See https://godoc.org/golang.org/x/tools/cmd/godex for more information.

%files    godex
%license LICENSE
%doc README.md
%{_bindir}/godex

#-----------------------------------------------------------------------

%package        benchcmp
Summary:        Displays performance changes between benchmarks for the Go programming language

%description    benchcmp
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/benchcmp for more information.

%files    benchcmp
%license LICENSE
%doc README.md
%{_bindir}/benchcmp

#-----------------------------------------------------------------------

%package        bundle
Summary:        Creates a single-source-file version of a source package

%description    bundle
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/bundle for more information.

%files    bundle
%license LICENSE
%doc README.md
%{_bindir}/gobundle

#-----------------------------------------------------------------------

%package        eg
Summary:        Example-based refactoring for the Go programming language

%description    eg
%{summary}.

See `eg -help` for more information.

%files    eg
%license LICENSE
%doc README.md
%{_bindir}/eg

#-----------------------------------------------------------------------

%package        file2fuzz
Summary:        Convert binary files to the Go fuzzing corpus format

%description    file2fuzz
%{summary}.

%files    file2fuzz
%license LICENSE
%doc README.md
%{_bindir}/file2fuzz

#-----------------------------------------------------------------------

%package        fiximports
Summary:        Fixes import declarations to use the canonical import path

%description    fiximports
%{summary}.

%files    fiximports
%license LICENSE
%doc README.md
%{_bindir}/fiximports

#-----------------------------------------------------------------------

%package        getgo
Summary:        Installs Go to the user's system

%description    getgo
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/getgo for more information.

%files    getgo
%license LICENSE
%doc README.md
%{_bindir}/getgo

#-----------------------------------------------------------------------

%package        go-contrib-init
Summary:        Helps new Go contributors get their development environment set up

%description    go-contrib-init
The go-contrib-init command helps new Go contributors get their development
environment set up for the Go contribution process.

It aims to be a complement or alternative to
https://golang.org/doc/contribute.html.

%files    go-contrib-init
%license LICENSE
%doc README.md
%{_bindir}/go-contrib-init

#-----------------------------------------------------------------------

%package        goimports
Summary:        Go programming language import line formatter

%description    goimports
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/goimports for more information.

%files    goimports
%license LICENSE
%doc README.md
%{_bindir}/goimports

#-----------------------------------------------------------------------

%package        gomvpkg
Summary:        Tool to move Go packages, updating import declarations

%description    gomvpkg
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/gomvpkg for more information.

%files    gomvpkg
%license LICENSE
%doc README.md
%{_bindir}/gomvpkg

#-----------------------------------------------------------------------

%if ! %{with bootstrap2}
%package        gopls
Summary:        LSP server for Go

%description    gopls
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/gopls for more information.

%files    gopls
%license LICENSE
%doc README.md
%{_bindir}/gopls
%endif

#-----------------------------------------------------------------------

%package        guru
Summary:        Tool for answering questions about Go source code

%description    guru
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/guru for more information.

%files    guru
%license LICENSE
%doc README.md
%{_bindir}/guru

#-----------------------------------------------------------------------

%package        present
Summary:        Display slide presentations and articles

%description    present
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/present for more information.

%files    present
%license LICENSE
%doc README.md
%{_bindir}/present

#-----------------------------------------------------------------------

%package        splitdwarf
Summary:        Uncompress and copy the DWARF segment of a Mach-O executable into the "dSYM" file

%description    splitdwarf
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/splitdwarf for more information.

%files    splitdwarf
%license LICENSE
%doc README.md
%{_bindir}/splitdwarf

#-----------------------------------------------------------------------

%package        ssadump
Summary:        Tool for displaying and interpreting the SSA form of Go programs

%description    ssadump
%{summary}.

%files    ssadump
%license LICENSE
%doc README.md
%{_bindir}/ssadump

#-----------------------------------------------------------------------

%package        stress
Summary:        Tool for catching sporadic failures

%description    stress
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/stress for more information.

%files    stress
%license LICENSE
%doc README.md
%{_bindir}/stress

#-----------------------------------------------------------------------

%package        toolstash
Summary:        Provides a way to save, run, and restore a known good copy of the Go toolchain

%description    toolstash
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/toolstash for more information.

%files    toolstash
%license LICENSE
%doc README.md
%{_bindir}/toolstash

#-----------------------------------------------------------------------

%package        goyacc
Summary:        Goyacc is a version of yacc for Go

%description    goyacc
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/goyacc for more information.

%files    goyacc
%license LICENSE
%doc README.md
%{_bindir}/goyacc

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n tools-%{version}

rm -rf vendor

%if %{with bootstrap2}
tar xf %{S:3}
%endif

%build
%gobuildroot
for cmd in %auth_commands; do
  %gobuild -o _bin/$(basename $cmd) %{goipath}/cmd/auth/$cmd
done
for cmd in %commands; do
  %gobuild -o _bin/$(basename $cmd) %{goipath}/cmd/$cmd
done
%if ! %{with bootstrap2}
%gobuild -o _bin/gopls %{goipath}/gopls
%endif

%install
%goinstall
for cmd in $(ls -1 _bin) ; do
	install -Dpm 0755 _bin/$cmd %{buildroot}%{_bindir}/$cmd
done

# fix conflict with rubygem-bundler
mv %{buildroot}%{_bindir}/bundle %{buildroot}%{_bindir}/gobundle

%check
%if %{with check}
%gochecks -t cmd -d imports -t internal/lsp -d go/pointer -d internal/imports -t gopls/internal -d internal/packagesdriver -d go/packages
%endif

