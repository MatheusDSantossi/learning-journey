import jakarta.persistence.*;
import lombok.*;

import java.time.LocalDateTime;

public interface OrderRepository extends JpaRepository<OrderEntity, Long> {
    boolean existsByOrderId(String orderId);
}
