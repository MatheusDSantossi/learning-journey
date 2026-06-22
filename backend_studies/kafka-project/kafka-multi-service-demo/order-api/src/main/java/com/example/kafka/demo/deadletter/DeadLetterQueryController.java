package com.example.kafka.demo.deadletter;
// package com.example.kafka.demo.controller;

// import com.example.kafka.demo.entity.DeadLetterEvent;
// import com.example.kafka.demo.entity.DeadLetterStatus;
// import com.example.kafka.demo.repository.DeadLetterEventRepository;
// import org.springframework.web.bind.annotation.*;

// import java.util.List;

// @RestController
// @RequestMapping("/admin/dlt")
// public class DeadLetterQueryController {
//     private final DeadLetterEventRepository repository;

//     public DeadLetterQueryController(DeadLetterEventRepository repository) {
//         this.repository = repository;
//     }


//     @GetMapping("/pending")
//     public List<DeadLetterEvent> listPending() {
//         return repository.findByStatusOrderByFailedAtDesc(DeadLetterStatus.PENDING);
//     }

//     @GetMapping("/all")
//     public List<DeadLetterEvent> listAll() {
//         return repository.findAll();
//     }
// }
