public class InsertDeleteAndGetRandom {
    class RandomizedSet {

    private Set<Integer> list;

    public RandomizedSet() {
        this.list = new HashSet<>();
    }

    public boolean insert(int val) {
        if (this.list.contains(val)) {
            return false;
        }
        this.list.add(val);
        return true;
    }
    
    public boolean remove(int val) {
        if(this.list.contains(val)) {
            this.list.remove(val);
            return true;
        }

        return false;
    }
    
    public int getRandom() {
        Random random = new Random();
        int listSize = this.list.size();

        int randomN = random.nextInt(listSize);

        ArrayList<Integer> listFromSet = new ArrayList<>(this.list);        

        return listFromSet.get(randomN);
    }
}
}

class CommunitySolution() {
    class RandomizedSet {

    private ArrayList<Integer> list;
    private Map<Integer, Integer> map;

    public RandomizedSet() {
        this.list = new ArrayList<>();
        this.map = new HashMap<>();
    }

    public boolean search(int val) {
        return map.containsKey(val);
    }

    public boolean insert(int val) {
        if(search(val)) return false;
        
        this.list.add(val);
        map.put(val, list.size() - 1);
        return true;
    }
    
    public boolean remove(int val) {
        if(!search(val)) return false;

        int index = map.get(val);
        list.set(index, list.get(list.size() - 1));
        map.put(list.get(index), index);
        list.remove(list.size() - 1);
        map.remove(val);

        return true;
    }
    
    public int getRandom() {
        Random random = new Random();
        
        return this.list.get(random.nextInt(this.list.size()));
    }
}
}
