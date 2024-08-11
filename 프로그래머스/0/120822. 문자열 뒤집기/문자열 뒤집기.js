function solution(my_string) {
    let characters = my_string.split('');
    let Rcharacters = characters.reverse();
    let Rstring = Rcharacters.join('');
    
    return Rstring;
}