Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"
  config.vm.box_version = "2004.01"

#   config.vm.synced_folder "./config", "/vagrant/config", mount_options: ["dmode=774", "fmode=775"]


#   # Load Balancer (Nginx)
  config.vm.define "lb" do |web|
    web.vm.hostname = "lb"
    web.vm.network "public_network", bridge: "wlp58s0", ip: "192.168.50.220"
    web.vm.network "forwarded_port", guest: 80, host: 8081
    web.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
      vb.cpus = 1
    end
    web.vm.provision "shell", inline: <<-SHELL
      sudo sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
      sudo sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
      sudo rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
      sudo rpm --import https://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-7
      sudo yum install -y epel-release
      sudo yum update -y
      sudo yum install python3 python3-pip -y
      # sudo yum install -y nginx curl
      # sudo systemctl daemon-reexec
      # sudo systemctl enable --now nginx
      # sudo systemctl enable --now firewalld
      # sudo firewall-cmd --permanent --add-service=http
      # sudo firewall-cmd --reload
      # sudo setenforce 0

      # Copy Load Balancer Nginx configuration
      # sudo cp /vagrant/config/nginx.conf /etc/nginx/nginx.conf
      # sudo systemctl restart nginx
    SHELL
  end
end
