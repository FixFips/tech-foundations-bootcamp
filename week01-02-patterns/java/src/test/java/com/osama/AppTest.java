package com.osama;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class AppTest {
    @Test
    void sanity() {
        assertEquals("OK", App.status());
    }
}
