import { useSyncExternalStore } from "react";
import { getCartState, subscribeToCart } from '../../../host/src/stores/cart.store';

export function useCart() {
    return useSyncExternalStore(
        subscribeToCart,
        getCartState,
    )
}