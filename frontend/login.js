function form_check(){
  var u_id = document.getElementById("u_id");
  var u_pwd = document.getElementById("u_pwd");

  if(!u_id.value){
    alert("아이디를 입력하세요.");
    u_id.focus();
    return false;
  };
  if(!u_pwd.value){
    alert("비밀번호를 입력하세요.");
    u_pwd.focus();
    return false;
  };
  return true;
};


let loginHTML = '';
loginHTML += `
  <style type="text/css">
    body,input{font-size:20px}
    fieldset{width:400px;}
    .label_txt{display:inline-block; width:80px;}
    button{width:80px; height:30px; font-size:14px; cursor:pointer; border:1px solid #999; font-size:14px; box-sizing:border-box; padding:0; background:#eee}
  </style>
  <form name="login_form" action="" method="post" onsubmit="return form_check()">
    <fieldset>
      <legend>로그인</legend>
      <p>
        <label for="u_id">아이디</label>
        <input type="text" name="u_id" id="u_id" class="txt">
      </p>
      <p>
        <label for="u_pwd">비밀번호</label>
        <input type="password" name="u_pwd" id="u_pwd" class="txt">
      </p>
      <p>
        <button type="submit">로그인</button>
        <button type="button" class="join_member" onclick="location.href='join.html'">회원가입</button>
      </p>
    </fieldset>
  </form>
`

var login = document.getElementById("login");
login.innerHTML = loginHTML;