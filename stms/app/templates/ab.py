<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
      rel="stylesheet"
    />
    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
    <link rel="stylesheet" href="css/all.min.css" />
    <link rel="stylesheet" href="css/index.css" />
    <link rel="stylesheet" href="css/registration2.css" />
    <link rel="stylesheet" href="css/gameregistration.css" />
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container-fluid">
          <a href="#" class="navbar-brand">Home</a>
          <button
            type="button"
            class="navbar-toggler"
            data-bs-toggle="collapse"
            data-bs-target="#navbarCollapse"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarCollapse">
            <div class="navbar-nav">
              <a href="#" class="nav-item nav-link">Tournament</a>
              <a href="#" class="nav-item nav-link">News</a>
              <a href="#" class="nav-item nav-link">About Us</a>
              <a href="#" class="nav-item nav-link">Contact Us</a>
            </div>
            <!-- <div class="navbar-nav ms-auto">
                          <a class="loginbtn nav-link" onclick="document.getElementById('login-form').style.display='block'" style="width:auto;">Login</a>
                      </div> -->
          </div>
        </div>
      </nav>

      
      <div class="container form-border my-5 mx-5 px-5 col-lg-7 d-flex justify-content-center mx-auto
        bg 
      " style="height: auto;">
      
      
  
            <form action ="" method="post" autocomplete="off" style="font-family: 'Libre Baskerville', serif;">
        
          <div class=" border-bottom my-3">
          <h5 class="d-flex text-center my-5 
      text-white justify-content-center" >Programming Contest</h5>
    </div>
              <div class="row g-3 my-2">
                <label for="teamname" class="col-sm-2 col-form-label " style="font-size: 0.8rem;"
                  >Team Name</label
                >
                <div class="col">
                  <input
                    type="text"
                    class="form-control rounded-pill  text-center input text-light"
                    placeholder="Enter Team Name"
                    aria-label="teamname"
                    name="teamname"
                    value=""
                    required

                  />
                </div>
                <label for="dept" class="col-sm-1 col-form-label ml-3   " style="font-size: 0.8rem;">Dept</label>
                <div class="col">
                  <select
                    class="form-select text-light rounded-pill input text-center"
                    id="validationCustom04"
                    aria-label="dept"
                    required
                    name="dept"
                    value=""
                  >
                    <!-- <option selected disabled value="">Choose...</option> -->
                    <option selected>CSE</option>
                    <option>Pharmacy</option>
                    <option>BBA</option>
                    <option>Law</option>
                    <option>Fashion Design</option>
                    <option>English</option>
                  </select>
                </div>
                
              </div>

              <div class="row g-3 my-2">
                <label for="captainname" class=" col-sm-2 col-form-label"style="font-size: 0.8rem;"
                  >Captain Name</label
                >
                <div class="col">
                  <input
                    type="text"
                    class="form-control rounded-pill  text-center text-light input"
                    placeholder="Enter Captain Name"
                    aria-label="captainname"
                    required
                    name="captainname"
                    value=""
                  />
                </div>
    
                <label for="id" class="col-sm-1 col-form-label " style="font-size: 0.8rem;">Id</label>
                <div class="col">
                  <input
                    type="tel"
                    class="form-control rounded-pill  text-center text-light"
                    placeholder="Enter id"
                    aria-label="id"
                    required
                    name="id"
                    value=""
                  />
                </div>
              </div>
    
              <!-- ...............................Other player.................................................... -->
<!--     
              <header class="text-center border-bottom my-4 ">
                <h6 class=" text-center text-light  my-4">Other Players</h6>
              </header> -->
    
              <div class="row g-3 my-2">
                <label for="name" class="col-sm-2 col-form-label " style="font-size: 0.8rem;"
                  >Member <span class="mx-2">1</label
                >
                <div class="col">
                  <input
                    type="text"
                    class="form-control rounded-pill text-light text-center"
                    placeholder="Enter name"
                    aria-label="name"
                    required
                    name="name"
                    value=""
                  />
                </div>
    
                <label for="id" class="col-sm-1 col-form-label " style="font-size: 0.8rem;">Id</label>
                <div class="col">
                  <input
                    type="tel"
                    class="form-control rounded-pill  text-center text-light "
                    placeholder="Enter id"
                    aria-label="id"
                    required
                    name="id"
                    value=""
                  />
                </div>
              </div>
              <div class="row g-3 my-2">
                <label for="name" class="col-sm-2 col-form-label "style="font-size: 0.8rem;"
                  >Member <span class="mx-2">2</label
                >
                <div class="col">
                  <input
                    type="text"
                    class="form-control rounded-pill  text-center text-light"
                    placeholder="Enter Name"
                    aria-label="name"
                    required
                    name="name"
                    value=""
                  />
                </div>
    
                <label for="id" class="col-sm-1 col-form-label "style="font-size: 0.8rem;">Id</label>
                <div class="col">
                  <input
                    type="tel"
                    class="form-control rounded-pill  text-center text-light"
                    placeholder="Enter id"
                    aria-label="id"
                    required
                    name="id"
                    value=""
                  />
                </div>
              </div>
              
              <!-- ............................Extra Player........................................ -->
              <header class="text-center border-bottom m-4 fw-bold">
                <!-- <button onclick="myFunction()">Extra players</button> -->
                 <h6 onclick="myFunction()" style="cursor: pointer;" class=" text-light">Extra players</h6>
                 <p style="font-size: 0.7rem;" class="text-light">Click to add Extra players</p>
                
              </header>
                  <div class="flex" id="myDIV" style=" display: none" >
              <div class="row g-3 my-2 e" >
                <label for="name" class="col-sm-2 col-form-label text-ligh" style="font-size: 0.8rem;"
                  >Member <span class="mx-2">3</label
                >
                <div class="col">
                  <input
                    type="text"
                    class="form-control rounded-pill  text-center text-ligh"
                    placeholder="Enter Name"
                    aria-label="name"
                    required
                    name="name"
                    value=""
                  />
                </div>
    
                <label for="id" class="col-sm-1 col-form-label " style="font-size: 0.8rem;">Id</label>
                <div class="col">
                  <input
                    type="tel"
                    class="form-control rounded-pill  text-center text-ligh"
                    placeholder="Enter id"
                    aria-label="id"
                    required
                    name="id"
                    value=""
                  />
                </div>
              </div>
              
    
            </div>
            <!-- <div class="my-5">
              <button type="submit" class="btn btn-primary mt-5 rounded-pill d-flex justify-content-center mx-auto">Submit</button>
            </div> -->
                
            
            <div class="my-4 ">
                <div class="   d-flex  d-flex justify-content-center mx-2">
                    <button type="submit" class="btn btn-primary mt-2 rounded-pill mx-2 px-3 py-2">Confirm</button>
                    <button type="submit" class="btn btn-primary mt-2 rounded-pill mx-2 px-3 py-2">Cancel</button>
                  </div>
            </div>
      
      
  
            
            </form>
        
          </div>
      </div>
    
      <script>
        function myFunction(myDIV) {
  var x = document.getElementById("myDIV");

  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}
     
  </script>
    
</body>
</html>