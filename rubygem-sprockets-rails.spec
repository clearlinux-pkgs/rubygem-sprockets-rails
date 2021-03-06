#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-sprockets-rails
Version  : 3.2.0
Release  : 13
URL      : https://rubygems.org/downloads/sprockets-rails-3.2.0.gem
Source0  : https://rubygems.org/downloads/sprockets-rails-3.2.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-actionpack
BuildRequires : rubygem-activesupport
BuildRequires : rubygem-railties
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-sass
BuildRequires : rubygem-sprockets
BuildRequires : rubygem-uglifier

%description
# Sprockets Rails
Provides Sprockets implementation for Rails 4.x (and beyond) Asset Pipeline.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n sprockets-rails-3.2.0
gem spec %{SOURCE0} -l --ruby > rubygem-sprockets-rails.gemspec

%build
export LANG=C
gem build rubygem-sprockets-rails.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
sprockets-rails-3.2.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/sprockets-rails-3.2.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/sprockets-rails-3.2.0/MIT-LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/sprockets-rails-3.2.0/README.md
/usr/lib64/ruby/gems/2.3.0/gems/sprockets-rails-3.2.0/lib/sprockets/rails.rb
/usr/lib64/ruby/gems/2.3.0/gems/sprockets-rails-3.2.0/lib/sprockets/rails/context.rb
/usr/lib64/ruby/gems/2.3.0/gems/sprockets-rails-3.2.0/lib/sprockets/rails/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/sprockets-rails-3.2.0/lib/sprockets/rails/quiet_assets.rb
/usr/lib64/ruby/gems/2.3.0/gems/sprockets-rails-3.2.0/lib/sprockets/rails/route_wrapper.rb
/usr/lib64/ruby/gems/2.3.0/gems/sprockets-rails-3.2.0/lib/sprockets/rails/task.rb
/usr/lib64/ruby/gems/2.3.0/gems/sprockets-rails-3.2.0/lib/sprockets/rails/utils.rb
/usr/lib64/ruby/gems/2.3.0/gems/sprockets-rails-3.2.0/lib/sprockets/rails/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/sprockets-rails-3.2.0/lib/sprockets/railtie.rb
/usr/lib64/ruby/gems/2.3.0/specifications/sprockets-rails-3.2.0.gemspec
