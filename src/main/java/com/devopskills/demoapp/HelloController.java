package com.devopskills.demoapp;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    @GetMapping("/")
    public String hello() {
        return "<h2>15.02.2023 <i><b>Hello DevOps Gurus :) !!!<b><i><h2>";
    }
}
