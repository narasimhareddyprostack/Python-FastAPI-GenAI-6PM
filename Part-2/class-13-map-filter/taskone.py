employees=[
  {"eid":1,"ename":"Shah Rukh Khan","gender":"Male","age":58,"salary":250000,"role":"Senior Architect","department":"Engineering"},
  {"eid":2,"ename":"Amitabh Bachchan","gender":"Male","age":81,"salary":300000,"role":"Chief Advisor","department":"Management"},
  {"eid":3,"ename":"Salman Khan","gender":"Male","age":58,"salary":220000,"role":"Operations Manager","department":"Operations"},
  {"eid":4,"ename":"Aamir Khan","gender":"Male","age":59,"salary":240000,"role":"Product Manager","department":"Product"},
  {"eid":5,"ename":"Akshay Kumar","gender":"Male","age":56,"salary":210000,"role":"Team Lead","department":"Engineering"},
  {"eid":6,"ename":"Hrithik Roshan","gender":"Male","age":50,"salary":200000,"role":"UI Architect","department":"Design"},
  {"eid":7,"ename":"Ranbir Kapoor","gender":"Male","age":41,"salary":180000,"role":"Software Engineer","department":"Engineering"},
  {"eid":8,"ename":"Ranveer Singh","gender":"Male","age":39,"salary":175000,"role":"Brand Manager","department":"Marketing"},
  {"eid":9,"ename":"Ajay Devgn","gender":"Male","age":55,"salary":230000,"role":"Delivery Head","department":"Operations"},
  {"eid":10,"ename":"Varun Dhawan","gender":"Male","age":36,"salary":160000,"role":"Frontend Developer","department":"Engineering"},
  {"eid":11,"ename":"Deepika Padukone","gender":"Female","age":38,"salary":190000,"role":"UX Lead","department":"Design"},
  {"eid":12,"ename":"Alia Bhatt","gender":"Female","age":31,"salary":165000,"role":"UI Developer","department":"Engineering"},
  {"eid":13,"ename":"Katrina Kaif","gender":"Female","age":40,"salary":185000,"role":"HR Manager","department":"HR"},
  {"eid":14,"ename":"Priyanka Chopra","gender":"Female","age":42,"salary":260000,"role":"Global Consultant","department":"Strategy"},
  {"eid":15,"ename":"Kareena Kapoor","gender":"Female","age":44,"salary":200000,"role":"Client Relationship Head","department":"Sales"},
  {"eid":16,"ename":"Anushka Sharma","gender":"Female","age":35,"salary":170000,"role":"Project Manager","department":"PMO"},
  {"eid":17,"ename":"Vidya Balan","gender":"Female","age":46,"salary":195000,"role":"Quality Lead","department":"QA"},
  {"eid":18,"ename":"Kangana Ranaut","gender":"Female","age":37,"salary":210000,"role":"Program Manager","department":"PMO"},
  {"eid":19,"ename":"Taapsee Pannu","gender":"Female","age":36,"salary":155000,"role":"Business Analyst","department":"Business"},
  {"eid":20,"ename":"Kiara Advani","gender":"Female","age":32,"salary":150000,"role":"Junior Analyst","department":"Business"},
  {"eid":21,"ename":"Rajinikanth","gender":"Male","age":74,"salary":320000,"role":"Chairman","department":"Board"},
  {"eid":22,"ename":"Kamal Haasan","gender":"Male","age":69,"salary":280000,"role":"Innovation Head","department":"R&D"},
  {"eid":23,"ename":"Vijay","gender":"Male","age":50,"salary":210000,"role":"Regional Manager","department":"Sales"},
  {"eid":24,"ename":"Ajith Kumar","gender":"Male","age":53,"salary":205000,"role":"Security Lead","department":"Admin"},
  {"eid":25,"ename":"Suriya","gender":"Male","age":49,"salary":195000,"role":"CSR Head","department":"CSR"},
  {"eid":26,"ename":"Dhanush","gender":"Male","age":41,"salary":175000,"role":"Backend Developer","department":"Engineering"},
  {"eid":27,"ename":"Vikram","gender":"Male","age":58,"salary":215000,"role":"Solution Architect","department":"Engineering"},
  {"eid":28,"ename":"Prabhas","gender":"Male","age":45,"salary":225000,"role":"Infrastructure Manager","department":"IT"},
  {"eid":29,"ename":"Mahesh Babu","gender":"Male","age":49,"salary":230000,"role":"Delivery Manager","department":"Operations"},
  {"eid":30,"ename":"Allu Arjun","gender":"Male","age":42,"salary":210000,"role":"Creative Director","department":"Design"},
  {"eid":31,"ename":"Nayanthara","gender":"Female","age":40,"salary":190000,"role":"Content Lead","department":"Media"},
  {"eid":32,"ename":"Samantha Ruth Prabhu","gender":"Female","age":37,"salary":185000,"role":"Wellness Program Head","department":"HR"},
  {"eid":33,"ename":"Rashmika Mandanna","gender":"Female","age":28,"salary":140000,"role":"Associate Consultant","department":"Strategy"},
  {"eid":34,"ename":"Pooja Hegde","gender":"Female","age":33,"salary":150000,"role":"Marketing Executive","department":"Marketing"},
  {"eid":35,"ename":"Tamannaah Bhatia","gender":"Female","age":34,"salary":155000,"role":"Campaign Manager","department":"Marketing"},
  {"eid":36,"ename":"Yash","gender":"Male","age":38,"salary":200000,"role":"Program Lead","department":"PMO"},
  {"eid":37,"ename":"Darshan","gender":"Male","age":47,"salary":195000,"role":"Operations Lead","department":"Operations"},
  {"eid":38,"ename":"Puneeth Rajkumar","gender":"Male","age":46,"salary":210000,"role":"Training Head","department":"L&D"},
  {"eid":39,"ename":"Kichcha Sudeep","gender":"Male","age":51,"salary":205000,"role":"Public Relations Head","department":"PR"},
  {"eid":40,"ename":"Mohanlal","gender":"Male","age":64,"salary":270000,"role":"Executive Director","department":"Management"}
]

#filter employees based on codition and store into new list.
male_employees_age40=[]

for emp in employees:
    if emp['gender']=="Male" and emp['age']<=40:
        male_employees_age40.append(emp)

print(len(male_employees_age40))

