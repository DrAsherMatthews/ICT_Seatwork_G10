from pyscript import document

def candiate_checker(e):
    club_members = ["lara rajj" , "sophia laforteza" , "yoonchae jeung" , "daniela avanizi" , "megan skiendiel" , "manon bannerman"]
    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f_name + ' ' + l_name

    member_checker = candidate.lower() in club_members
    messages = (f'Sorry {candidate}, your name is not on the list.', f'Congratulations! {candidate}, you are now part of the katseye club!')

    document.getElementById('result').innerHTML = messages[member_checker]