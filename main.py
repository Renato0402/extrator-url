# url = "https://bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real"
url = " "

#Sanitização da URL
url = url.strip()

if __name__ == '__main__':

    if url == "":
        raise ValueError("A URL está vazia")

    # Separa base e os parâmetros
    indice_interrogacao = url.find('?')
    url_base = url[0:indice_interrogacao]
    print(url_base)

    url_parametros = url[indice_interrogacao + 1:]
    print(url_parametros)

    # Busca o valor de um parâmetro
    parametro_busca = 'quantidade'
    indice_parametro = url_parametros.find(parametro_busca)
    indice_valor = indice_parametro + len(parametro_busca) + 1
    indice_e_comercial = url_parametros.find('&', indice_valor)
    indice_e_comercial = indice_e_comercial if indice_e_comercial != -1 else len(url_parametros)
    valor = url_parametros[indice_valor:indice_e_comercial]

    print(valor)
