$(document).ready(function(){ 
    $('.updateButton').on('click', function(event) {
        var sortType = $('#sortType').val();
        console.log("Sort Type : "+ sortType)

        var id = setInterval(frame, 1000)
        var count = 0
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
                    else if(data.sorted){
                        renderArray(data.array)
                        $('#resultMessage').text("Done").show()
                        clearInterval(id)
                    }
                    else{
                        renderArray(data.array)
                        $('#resultMessage').text("Sorting.. "+count).show()
                        count++
                    }
                    function renderArray(array){
                        for (var i = 0; i < 50; i++) {
                            newHeight = data.array[i]
                            elemid = "#arrayElement_"+i
                            $(elemid).css("height", newHeight)
                        }
                    }
                }
            });
        }
    });
});