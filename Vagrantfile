Vagrant.configure("2") do |config|
  config.ssh.insert_key = false

  config.vm.define "sonnh-lab" do |cf1|
    cf1.vm.box = "bento/ubuntu-18.04"
    cf1.vm.hostname ="sonnh-lab"
    cf1.vm.network :private_network, ip: "192.168.1.10"
    cf1.vm.provider "virtualbox" do |vb|
        vb.memory = "8000"
    end
  end

end

