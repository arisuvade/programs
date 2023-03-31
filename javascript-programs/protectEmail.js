function protectEmail(email) {
  let emailAddress = email.split("@");
  let username = `${emailAddress[0].slice(0, 5)}...`;
  let domainName = `@${emailAddress[1]}`;
  return username + domainName;
}

console.log(protectEmail("ariesbautista@gmail.com"));
console.log(protectEmail("davedumalay@yahoo.com"));
