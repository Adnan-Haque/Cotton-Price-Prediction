$(document).ready(function () {
    
        var val = $("#state").val();
        if (val == "Andhra Pradesh") {
            //Guntur
            $("#district").html("<option value='Guntur'>Guntur</option>");
            // Mungari  (Ginned)
            // N-44
            // Desi
            // MCU
            $('#variety').html("<option value= 'Mungari  (Ginned)'>Mungari  (Ginned)</option><option value= 'N-44'>N-44</option><option value= 'Desi'>Desi</option><option value= 'MCU'>MCU</option>");
        } 
        else if (val == "Gujarat") {
            // Amreli
            // Bhavnagar
            // Jamnagar
            // Junagarh
            $("#district").html("<option value='Amreli'>Amreli</option><option value='Bhavnagar'>Bhavnagar</option><option value='Jamnagar'>Jamnagar</option><option value='Junagarh'>Junagarh</option>");
            // Other
            // Shanker 6 (B) 30mm FIne
            // Shanker 4 31mm FIne
            // Cotton (Unginned)
            $('#variety').html("<option value= 'Other'>Other</option><option value= 'Shanker 6 (B) 30mm FIne'>Shanker 6 (B) 30mm FIne</option><option value= 'Shanker 4 31mm FIne'>Shanker 4 31mm FIne</option><option value= 'Cotton (Unginned)'>Cotton (Unginned)</option>");
        } 
        else if (val == "Maharashtra") {
            // Chandrapur
            // Hingoli
            // Jalana
            // Nagpur
            $("#district").html("<option value='Chandrapur'>Chandrapur</option><option value='Hingoli'>Hingoli</option><option value='Jalana'>Jalana</option><option value='Nagpur'>Nagpur</option>");
            // Other
            // Varalaxmi
            // LRA
            // H-4(A) 27mm FIne
            $('#variety').html("<option value= 'Other'>Other</option><option value= 'Varalaxmi'>Varalaxmi</option><option value= 'LRA'>LRA</option><option value= 'H-4(A) 27mm FIne'>H-4(A) 27mm FIne</option>");
        } 
        else if(val == "Rajasthan") {
            // Ajmer
            // Ganganagar
            // Hanumangarh
            $("#district").html("<option value='Ajmer'>Ajmer</option><option value='Ganganagar'>Ganganagar</option><option value='Hanumangarh'>Hanumangarh</option>");
            // 170-CO2 (Unginned)
            // Other
            // American
            // Desi
            $('#variety').html("<option value= '170-CO2 (Unginned)'>170-CO2 (Unginned)</option><option value= 'Other'>Other</option><option value= 'American'>American</option><option value= 'Desi'>Desi</option>");
        }
        else if(val == "Tamil Nadu") {
            // Dindigul
            // Erode
            // Madurai
            // Namakkal
            $("#district").html("<option value='Dindigul'>Dindigul</option><option value='Erode'>Erode</option><option value='Madurai'>Madurai</option><option value='Namakkal'>Namakkal</option>");
            // MCU 5
            // MCU-7
            // Other
            // LRA
            $('#variety').html("<option value= 'MCU 5'>MCU 5</option><option value= 'MCU-7'>MCU-7</option><option value= 'Other'>Other</option><option value= 'LRA'>LRA</option>");
        }
        else if(val == "Telangana") {
            // Adilabad
            // Karimnagar
            // Khammam
            // Warangal
            $("#district").html("<option value='Adilabad'>Adilabad</option><option value='Karimnagar'>Karimnagar</option><option value='Khammam'>Khammam</option><option value='Warangal'>Warangal</option>");
            // Cotton (Unginned)
            // H4
            // Cotton (Ginned)
            // Other
            $('#variety').html("<option value= 'Cotton (Unginned)'>Cotton (Unginned)</option><option value= 'H4'>H4</option><option value= 'Cotton (Ginned)'>Cotton (Ginned)</option><option value= 'Other'>Other</option>");
        }
        else if (val == "null") {
            $("#district").html("<option value=''>--select district--</option>");
            $('#variety').html("<option value=''>--select variety--</option>");
        }
    
});