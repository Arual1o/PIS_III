
  const CustomButton = () => <span className="octicon octicon-star" />;
  function insertStar() {
    const cursorPosition = this.quill.getSelection().index;
    this.quill.format(Weight: );
    this.quill.setSelection(cursorPosition + 1);

    /*Revisar: mandar json a la DB
    /*Crear una ruta para la tarjeta 
    /*Retornar información de la tarjeta que se quiere editar y rellenar los campos título y contenido