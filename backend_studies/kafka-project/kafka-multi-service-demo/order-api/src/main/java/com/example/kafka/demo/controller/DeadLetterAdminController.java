package com.example.kafka.demo.controller;

import com.example.kafka.demo.entity.DeadLetterEvent;
import com.example.kafka.demo.entity.DeadLetterStatus;
import com.example.kafka.demo.repository.DeadLetterEventRepository;
import com.example.kafka.demo.service.DeadLetterService;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/admin/dlt")
public class DeadLetterAdminController {
    private final DeadLetterService deadLetterService;
    private final DeadLetterEventRepository repository;

    public DeadLetterAdminController(DeadLetterService deadLetterService, DeadLetterEventRepository repository) {
        this.deadLetterService = deadLetterService;
        this.repository = repository;
    }

    @GetMapping("/pending")
    public List<DeadLetterEvent> listPending() {
        return repository.findByStatusOrderByFailedAtDesc(DeadLetterStatus.PENDING);
    }

    @GetMapping("/all")
    public List<DeadLetterEvent> listAll() {
        return repository.findAll();
    }

    @PostMapping("/{id}/replay")
    public DeadLetterEvent replay(@PathVariable Long id) {
        deadLetterService.replay(id);
        return repository.findById(id).orElseThrow(() -> new IllegalArgumentException("DLT event not found: " + id));
    }

    @PostMapping("/replay-pending")
    public Map<String, Object> replayPending() {
        int count = deadLetterService.replayAllPending();
        return Map.of("message", "Replay finished", "replayedCount", count);
    }

    @GetMapping
    public Map<String, Object> info() {
        return Map.of("availableEndpoints",
            List.of(
                "GET /admin/dlt",
                   "GET /admin/dlt/all",
                    "GET /admin/dlt/pending",
                    "POST /admin/dlt/{id}/replay",
                    "POST /admin/dlt/replay-pending"
            )
        );
    }
}
