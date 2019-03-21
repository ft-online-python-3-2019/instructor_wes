// Given a sequence of parentheses, braces and brackets, determine whether it is valid.Example: "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!" => true. "D(i{a}l[ t]o)n{e" => false. "A(1)s[O (n]0{t) 0}k" => false.
function bracesvalid(str){
  var open = [];
  var bracesMap = {
    "}": "{",
    ")": "(",
    "]": "[",
  };

  for(var i = 0; i <str.length;i++){
    if(str[i] === "(" || str[i] === "[" || str[i] === "{"){
      open.push(str[i])
    }
    if (str[i] === ")" || str[i] === "]" || str[i] === "}") {
      if(open.pop() !== bracesMap[str[i]]) {
        return false;
      }
    }
  }
  return open.length === 0;
}

console.log(bracesvalid("W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!"));
console.log(bracesvalid("D(i{a}l[ t]o)n{e"));
console.log(bracesvalid("A(1)s[O (n]0{t) 0}k"));