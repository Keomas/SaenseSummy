import sys
from handle_page_saense import HandlePage
import phpaiola_pt5_temario





def main():
    # Funcao principal da aplicacao #
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        print("""      
        Resuma posts do Portal saense ( https://saense.com.br/ )

        Uso: python saense_summy <URL do Artigo>
        """)
        exit()
    else:
        url = sys.argv[1]
    
    page=HandlePage(url)
    page.getSoup()
    page.getTitulo()
    print("#### Getting article: "+page.titulo)
    page.getTexto() 
    page.getAutor()
    page.getData()

    text_to_resume=page.text
    
    print("#### Running summarization #### ")

    summy=phpaiola_pt5_temario.summarize(text_to_resume)

    print("Summary: \n"+summy)

if __name__ == "__main__":
    main()
