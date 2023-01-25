package com.devopskills.demoapp;

import io.dekorate.kubernetes.annotation.KubernetesApplication;
import io.dekorate.kubernetes.annotation.Label;
import io.dekorate.kubernetes.annotation.Port;
import io.dekorate.kubernetes.annotation.ServiceType;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Service;

@SpringBootApplication
@KubernetesApplication(
		ports = @Port(name = "http", containerPort = 9090),
		labels = @Label(key = "version", value = "v1"),
		serviceType = ServiceType.LoadBalancer,
		replicas = 4

)
public class DemoAppApplication {

	public static void main(String[] args) {
		SpringApplication.run(DemoAppApplication.class, args);
	}

}
