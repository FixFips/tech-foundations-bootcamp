package com.osama.singleton;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class ConfigTest {
    @Test
    void singletonIdentity() {
        Config a = Config.getInstance();
        Config b = Config.getInstance();
        assertSame(a, b);
        assertEquals("dev", a.getName());
    }
}
