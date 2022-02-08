document.addEventListener("DOMContentLoaded", function(){
  first_page_sh();
});

function first_page_sh(){
  document.getElementById("first_join").style.display="block";
  document.getElementById("btn_next").style.display="block";
  document.getElementById("second_join").style.display="none";
  document.getElementById("btn_submit").style.display="none";
  document.getElementById("btn_back").style.display="none";
}

function second_page_sh(){
  document.getElementById("first_join").style.display="none";
  document.getElementById("btn_next").style.display="none";
  document.getElementById("btn_back").style.display="block";
  document.getElementById("second_join").style.display="block";
  document.getElementById("btn_submit").style.display="block";
}

function second_page(){
  var u_name = document.getElementById("u_name");
  var u_id = document.getElementById("u_id");
  var u_pwd = document.getElementById("u_pwd");
  var re_pwd = document.getElementById("re_pwd");

  if(!u_name.value){
    alert("이름을 입력하세요.");
    u_name.focus();
    return false;
  };

  if(!u_id.value){
    alert("아이디를 입력하세요.");
    u_id.focus();
    return false;
  };

  if(u_id.value.length < 4 || u_id.value.length > 12){
    alert("아이디는 4~12글자만 입력할 수 있습니다.");
    u_id.focus();
    return false;
  };

  if(!u_pwd.value){
    alert("비밀번호를 입력하세요.");
    u_pwd.focus();
    return false;
  };
  if(u_pwd.value.length < 4 || u_pwd.value.length > 8){
    alert("비밀번호는 4~8글자만 입력할 수 있습니다.");
    u_pwd.focus();
    return false;
  };

  if(u_pwd.value != re_pwd.value){
    alert("비밀번호를 확인해주세요.");
    re_pwd.focus();
    return false;
  };
  second_page_sh();
}
  
function form_check(){
  var major = document.getElementById("major");
  var degree = document.getElementById("degree");
  var organization = document.getElementById("organization");
  var career = document.getElementById("career");
  var email_id = document.getElementById("email_id");

  if(!major.value){
    alert("전공을 입력하세요.");
    major.focus();
    return false;
  };

  if(!degree.value){
    alert("학위를 입력하세요.");
    degree.focus();
    return false;
  };

  if(!organization.value){
    alert("소속을 입력하세요.");
    organization.focus();
    return false;
  };

  if(!career.value){
    alert("경력을 입력하세요.");
    career.focus();
    return false;
  };

  if(!email_id.value){
    alert("이메일을 입력하세요.");
    email_id.focus();
    return false;
  };
  
  return true;
};

function select_email(){
  var email_dns = document.getElementById("email_dns");
  var email_sel = document.getElementById("email_sel");

  var idx = email_sel.options.selectedIndex;
  var rtn_val = email_sel.options[idx].value;

  email_dns.value = rtn_val;
};

let joinHTML = '';
joinHTML += `
  <style type="text/css">
    body,input,select,option,button{font-size: 16px;}
    button{cursor:pointer}
    input[type=checkbox]{width: 16px; height: 16px; vertical-align: middle;}
    input[type=text]{border: 1px solid #999; padding: 3px;}
    input[type=password]{border: 1px solid #999; padding: 3px;}
    p{margin-bottom:24px}
    .label_txt{display: inline-block; width: 120px;}
    .ex_txt{margin-left: 130px; color: #989898; font-size: 14px;}
    .btn_idCheck{width: 80px;height: 26px;border: 1px solid #999;font-size: 14px;box-sizing: border-box; padding: 0; background: #eee;}
    .btn_addr{width: 80px;height: 26px;border: 1px solid #999;font-size: 14px;box-sizing: border-box; padding: 0; background: #eee;}
    .postal_code{width: 80px;}
    .addr1{width: 350px; margin-bottom: 24px;}
    .addr2{width: 350px;}
    .btn_submit{float:left; margin-right:8px; width: 80px;height: 26px;border: 1px solid #999;font-size: 14px;box-sizing: border-box; padding: 0; background: #eee;}
    .btn_back{width: 80px;height: 26px;border: 1px solid #999;font-size: 14px;box-sizing: border-box; padding: 0; background: #eee;}
  </style>

  <form name="join_form" action="" method="get" onsubmit="return form_check()">
  <fieldset>
    <p style="color: red;">* 는 필수 입력 항목입니다.</p>
    <legend>회원가입</legend>
    <div id="first_join">
      <p>
        <label for="u_name" class="label_txt">* 이름</label>
        <input type="text" name="u_name" id="u_name" class="u_name">
      </p>

      <p>
        <label for="u_id" class="label_txt">* 아이디</label>
        <input type="text" name="u_id" id="u_id" class="u_id">
        <button type="button" class="btn_idcheck" onclick="search_id()">아이디 중복확인</button>
        <br>
        <span class="ex_txt">아이디는 4~12글자만 입력할 수 있습니다.</span>
      </p>

      <p>
        <label for="u_pwd" class="label_txt">* 비밀번호</label>
        <input type="password" name="u_pwd" id="u_pwd" class="u_pwd">
        <br>
        <span class="ex_txt">비밀번호는 4~8글자만 입력할 수 있습니다.</span>
      </p>

      <p>
        <label for="re_pwd" class="label_txt">* 비밀번호 확인</label>
        <input type="password" name="re_pwd" id="re_pwd" class="re_pwd">
      </p>

      <p>
        <label for="mobile" class="label_txt">전화번호</label>
        <input type="tel" name="mobile" id="mobile" class="mobile">
        <br>
        <span class="ex_txt">"-" 없이 숫자만 입력</span>
      </p>
      
      <p>
        <label for="birth" class="label_txt">생년월일</label>
        <input type="datetime" name="birth" id="birth" class="birth">
        <br>
        <span class="ex_txt">ex) 20210608</span>
      </p>
    </div>

    <div id="second_join">
      <p>
        <label for="major" class="label_txt">* 전공</label>
        <input type="text" name="major" id="major" class="major">
      </p>

      <p>
        <label for="degree" class="label_txt">* 학위</label>
        <input type="text" name="degree" id="degree" class="degree">
      </p>

      <p>
        <label for="organization" class="label_txt">* 소속</label>
        <input type="text" name="organization" id="organization" class="organization"><br>
        <span class="ex_txt">OO대학교 / OOO연구소</span>
      </p>

      <p>
        <label for="career" class="label_txt">* 경력</label>
        <input type="number" name="career" id="career" class="career"><br>
        <span class="ex_txt">O년</span>
      </p>

      <!-- <p>
        <label for="email_id" class="label_txt">이메일</label>
        <input type="text" name="email_id" id="email_id" class="email_id"> @
        <input type="text" name="email_dns" id="email_dns" class="email_dns">
        <select name="email_sel" id="email_sel" class="email_sel" onchange="select_email()">
          <option value="">직접 입력</option>
          <option value="naver.com">naver.com</option>
          <option value="daum.net">daum.net</option>
          <option value="gmail.com">gmail.com</option>
        </select>        
      </p> -->

      <p>
        <label for="email_id" class="label_txt">* 이메일</label>
        <input type="email" name="email_id" id="email_id" class="email_id">
        <br>
        <span class="ex_txt">abcd@efgh.com</span>
      </p>
    </div>

      <p>
        <button type="button" class="btn_next" id="btn_next" onclick="second_page()">다음</button>
        <button type="submit" class="btn_submit" id="btn_submit">가입하기</button>
        <button type="button" class="btn_back" id="btn_back" onclick="first_page_sh()">이전</button>
      </p>
  </fieldset>
  </form>
`

var join = document.getElementById("join");
join.innerHTML = joinHTML;