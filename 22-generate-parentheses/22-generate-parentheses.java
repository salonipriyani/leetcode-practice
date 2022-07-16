class ParenthesisString{
    String str;
    int openCount;
    int closeCount;

    public ParenthesisString(String s, int oCount, int cCount){
        str = s;
        openCount = oCount;
        closeCount = cCount; 
    }
}
class Solution {
    
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        Queue<ParenthesisString> q = new LinkedList<>();
        q.offer(new ParenthesisString("", 0, 0));
        while(!q.isEmpty()){
            ParenthesisString currStr = q.poll();
            if (currStr.openCount == n && currStr.closeCount == n)
                res.add(currStr.str);
            else{
                if(currStr.openCount < n)
                    q.offer(new ParenthesisString(currStr.str + "(", currStr.openCount+1, currStr.closeCount));
                if(currStr.closeCount < currStr.openCount)
                    q.offer(new ParenthesisString(currStr.str + ")", currStr.openCount, currStr.closeCount + 1));
            }
        }
        return res;
    }
}