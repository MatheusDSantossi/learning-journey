package com.example.kafka.demo.controller;

import com.example.kafka.demo.service.DeadLetterService;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/admin/dlt")
public class DeadLetterAdminController {
    private final DeadLetterService deadLetterService;

    public DeadLetterAdminController(DeadLetterService deadLetterService) {
        this.deadLetterService = deadLetterService;
    }

    @PostMapping("/{id}/replay")
    public String replay(@PathVariable Long id) {
        deadLetterService.replay(id);
        return "Replayed DLT event with id " + id;
    }
}
