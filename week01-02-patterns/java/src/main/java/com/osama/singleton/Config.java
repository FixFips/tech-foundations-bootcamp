package com.osama.singleton;

public class Config {
    private final String name;

    private Config(String name) {
        this.name = name;
    }

    // Static-holder idiom: thread-safe lazy initialization without sync cost.
    private static class Holder {
        private static final Config INSTANCE = new Config("dev");
    }

    public static Config getInstance() {
        return Holder.INSTANCE;
    }

    public String getName() {
        return name;
    }
}
