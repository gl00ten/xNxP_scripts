# puppet_desktop_packages.pp
# Old Puppet manifest snippet for "uniformizing" a desktop VM / dev machine.
# Mixed with shell commands (invalid in manifest) and notes.
# Kept for historical reference only. Do not apply directly.

class puppetEnvironmentTest {
  # stuff missing from virtual machines
  $wantedPackages = ['ntp','curl','htop','ssh', 'sshfs', 'git','nmap','hexchat','libreoffice','pulseaudio','workrave','virtualbox','keepassx']
  package { $wantedPackages: ensure => installed }
 
 
 #finish installing language support
 sudo apt install $(check-language-support)
  
  #~~~~~~
  #this will probably break puppet-master, use on an agent, or a separate machine
  
  # puppet test stuff
  #$puppetRakeTestPackages = ['ruby-dev','gem-dev','ruby','gem','bundler','libxslt-dev','libxml2-dev','build-essential','libxslt-dev','libxml2-dev',]
  #package { $puppetRakeTestPackages: ensure => installed }
  
  #then in in the module's to be tested root directory (after alterations and tests have been written)
  #bundle install
  #bundle exec rake
  #~~~~~~ 
  
  # this wont work, something about not having gem, btw, installing gem tends to break puppet to. joy!
  package { 'puppet-lint':
	  ensure   => '1.1.0',
	  provider => 'gem',
  }

  # this works? i think it requires some module
  #class { locales: default_value => 'C', }
  #}

}
