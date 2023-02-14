package com.devopskills.demoapp;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    @GetMapping("/")
    public String hello() {
        return "<h2><i><b>Hello DevOps Upskill !!!<b><i><h2> New 20";
    }
}
