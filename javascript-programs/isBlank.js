function isBlank(string) {
  if (string == "") {
    return true;
  } else {
    return false;
  }
}

console.log(isBlank(""));
console.log(isBlank("abc"));
