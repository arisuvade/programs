function strParameterize(string) {
  return string.toLowerCase().replace(".", "").split(" ").join("-");
}

console.log(strParameterize("Aries Bautista from Pampanga."));
console.log(strParameterize("Dave Dumalay from Bulacan."));
