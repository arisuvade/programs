function abbrevName(name) {
  let fullName = name.split(" ");
  let firstName = fullName[0];
  let lastNameInitial = `${fullName[1][0]}.`;
  return `${firstName} ${lastNameInitial}`;
}

console.log(abbrevName("Aries Bautista"));
console.log(abbrevName("Dave Dumalay"));
