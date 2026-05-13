class CommunitySolution {
    public List<String> wordBreak(String s, List<String> wordDict) {
        Set<String> dict = new HashSet<>(wordDict);
        List<String> res = new ArrayList<>();
        List<String> cur = new ArrayList<>();
        helper(s, 0, dict, cur, res);
        return res;
    }

    private void helper (String s, int i, Set<String> dict, List<String> cur, List<String> res) {

        if (i == s.length()) {
            if (cur.size() > 0) {
                StringBuilder sb = new StringBuilder();
                for (int j = 0; j < cur.size(); j++) {
                    if (j > 0) {
                        sb.append(" ");
                    }

                    sb.append(cur.get(j));
                 }
                 res.add(sb.toString());
            }
            return;
        }
        for (int j = i+1; j <= s.length(); j++) {
            if (dict.contains(s.substring(i, j))) {
                cur.add(s.substring(i, j));
                helper(s, j, dict, cur, res);
                cur.remove(cur.size() - 1);
            }
        }
    }
}

class YouTubeTutorialSolution {
    Map<String, List<String>> memoryMap = HasMap<>();
    public List<String> wordBreak(String s, List<String> wordDict) {
        List<String> result = new ArrayList<>();
        if (s == null || s.length() == 0) return;        

        if (memoryMap.containsKey(s)) {
            return memoryMap.get(s);
        }

        if (wordDict.contains(s)) {
            result.add(s);
        }

        for (int i = 0; i < s.length(); i++) {
            String tmp = s.substring(i);
            if (wordDict.contains(tmp)) {
                List<String> temp = wordBreak(s.substring(0, i), wordDict);
                if (temp.size() > 0) {
                    for (int j = 0; j < temp.size(); j++) {
                        result.add(temp.get(j)+ " " + tmp);
                    }
                }
            }
        }

        memoryMap.put(s, result);
        return result;
    } 
}
