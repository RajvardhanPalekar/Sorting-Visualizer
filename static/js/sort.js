$(document).ready(function(){ 
    $('.updateButton').on('click', function(event) {
        var sortType = $('#sortType').val();
        console.log("Sort Type : "+ sortType)

        var id = setInterval(frame, 100)
        function frame(){
            $.ajax({
                url : '/sort',
                type : 'POST',
                data : {
                    sortType : sortType
                },
                success: function(data){
                    if(data.error) {
                        $('#resultMessage').text(data.error).show()
                    }
                    else {
                        array_object = data.array_object
                        if(array_object.sorted == true){
                            renderArray(array_object)
                            $('#resultMessage').text("Done").show()
                            clearInterval(id)
                        }
                        else{
                            renderArray(array_object)
                            $('#resultMessage').text("Sorting..").fadeIn(1000).fadeOut(1000).show()
                        }
                    }
                    function renderArray(array_object){
                        for (var i = 0; i < 30; i++) {
                            newHeight = array_object.array[i]
                            elemid = "#arrayElement_"+i
                            $(elemid).css("height", newHeight)

                            if(array_object.sorted_array.includes(i)){
                                $(elemid).css("background-color", "darkslategray")
                            }
                            else {
                                $(elemid).css("background-color", "blue")
                            }
                            if(i == array_object.current || i == array_object.current+1){
                                $(elemid).css("background-color", "greenyellow")
                            }
                            if(array_object.swap && array_object.swap.includes(i)){
                                $(elemid).css("background-color", "red")
                            }
                            
                        }
                    }
                }
            });
        }
    });
});