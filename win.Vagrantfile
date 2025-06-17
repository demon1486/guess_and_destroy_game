# -*- mode: ruby -*-
# vi: set ft=ruby :

# Lightweight Windows 10 version with WinRM enabled RDP on port 33899
# user: vagrant password: vagrant

Vagrant.configure(2) do |config|
  config.vm.box = "xnohat/windows10lite"
  config.vm.box_version = "1.0.0"
  config.vm.guest = :windows
  config.vm.communicator = "winrm"
  config.vm.boot_timeout = 600
  config.vm.graceful_halt_timeout = 600

  config.vm.network :forwarded_port, guest: 33899, host: 33899

  config.vm.provider "virtualbox" do |vm|
      vm.name = "vagrant-pc"
      vm.gui = true
      vm.cpus = 2
      vm.memory = 2048
  end
end
