class Solution {
    public List<Integer> diffWaysToCompute(String expression) {
        List<Integer> res = new ArrayList<>();
        if (!expression.contains("+") && !expression.contains("*") && !expression.contains("-"))
            res.add(Integer.parseInt(expression));
        else{
            for (int i = 0; i < expression.length(); i++){
                char curr = expression.charAt(i);
                if (!Character.isDigit(curr)){
                    List<Integer> leftParts = diffWaysToCompute(expression.substring(0, i));
                    List<Integer> rightParts = diffWaysToCompute(expression.substring(i+1));
                    for (int left: leftParts){
                        for (int right: rightParts){
                            if (curr == '+')
                                res.add(left + right);
                            else if (curr == '-')
                                res.add(left - right);
                            else
                                res.add(left * right);
                        }
                    }
                }
            }
        }
        
        return res;
    }
}