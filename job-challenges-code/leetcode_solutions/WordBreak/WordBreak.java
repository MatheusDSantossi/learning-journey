class MySolution {
    public boolean wordBreak(String s, List<String> wordDict) {
        String splittedWord = s;
        // System.out.println(wordDict);
        // System.out.println(s);

        for (String word : wordDict) {
            System.out.println(splittedWord.split(word)[0]);
            System.out.println(splittedWord.split(word)[1]);
            if (s.split(word)[0] != null && s.split(word)[0].length() >= 1) {
                splittedWord = s.split(word)[0];
            } else {
                System.out.println("Word: " + word);
                return false;
            }
        }

        System.out.println(splittedWord);
        return true;
    }
}

// !Important a huge learn, start simple and separate the solution in another
// function
class CommunitySolution {
    public boolean wordBreak(String s, List<String> wordDict) {
        // Put all words into a HashSet
        Set<String> set = new HashSet<>(wordDict);
        return wb(s, set);
    }

    private boolean wb(String s, Set<String> set) {
        int len = s.length();
        if (len == 0) {
            return true;
        }

        for (int i = 1; i <= len; i++) {
            if (set.contains(s.substring(0, i)) && wb(s.substring(i), set)) {
                return true;
            }
        }
        return false;
    }
}

// AI Solution (the previous one got time-limit error)
class CommunitySolutionAI {
    public boolean wordBreak(String s, List<String> wordDict) {
        // Put all words into a HashSet
        Set<String> set = new HashSet<>(wordDict);
        Map<String, Boolean> memo = new HashMap<>();
        return wb(s, set, memo);
    }

    private boolean wb(String s, Set<String> set, Map<String, Boolean> memo) {
        if (s.isEmpty())
            return true;
        if (memo.containsKey(s))
            return memo.get(s);

        for (int i = 1; i <= s.length(); i++) {
            String prefix = s.substring(0, i);

            if (set.contains(prefix) && wb(s.substring(i), set, memo)) {
                memo.put(s, true);
                return true;
            }
        }
        memo.put(s, false);
        return false;
    }
}
