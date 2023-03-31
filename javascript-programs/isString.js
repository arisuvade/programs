function isString(input) {
  if (typeof input == "string") {
    return true;
  } else {
    return false;
  }
}

console.log(isString("w3resource"));
console.log(isString(1234));
