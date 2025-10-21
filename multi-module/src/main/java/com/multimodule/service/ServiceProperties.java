package com.multimodule.service;

import org.springframework.boot.context.properties.ConfigurationProperties;

@ConfigurationProperties
public class ServiceProperties {
    private String message = "Hello, world!";

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
}
