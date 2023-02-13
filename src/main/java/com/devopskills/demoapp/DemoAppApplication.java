package com.devopskills.demoapp;

import io.dekorate.kubernetes.annotation.*;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@KubernetesApplication(
		ports = @Port(name = "http", containerPort = 9090),
		labels = @Label(key = "version", value = "v1"),
		initContainers = @Container(image="nbglink/demo-app:jma-11", imagePullPolicy = ImagePullPolicy.Always),
		serviceType = ServiceType.LoadBalancer,
		replicas = 3

)
public class DemoAppApplication {

	public static void main(String[] args) {
		SpringApplication.run(DemoAppApplication.class, args);
	}

}
