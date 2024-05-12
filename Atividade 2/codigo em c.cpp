#include <iostream>
#include <string>

class No{
    private:
        int numero;
        No* ponteiro;
    public:
        No(int numero){
            this->numero = numero;
            this->ponteiro = nullptr;
        }
        int getNumero(){
            return this->numero;
        }
        No* getPonteiro(){
            return this->ponteiro;
        }
        void setPonteiro(No* ponteiro){
            this->ponteiro = ponteiro;
        }
};
class L_Ligada{
    private:
        No* cabeca;
    public:
        L_Ligada(){
            this->cabeca = nullptr;
        }
        void adicionar(int numero, int posicao){
            No* novo = new No(numero);
            if(posicao == 0){
                novo->setPonteiro(this->cabeca);
                this->cabeca = novo;
            }else{
                No* anterior = this->cabeca;
                for(int i = 0; i < posicao - 1; i++){
                    anterior = anterior->getPonteiro();
                }
                novo->setPonteiro(anterior->getPonteiro());
                anterior->setPonteiro(novo);
            }
        }
        void remover(int numero){
            No* anterior = nullptr;
            No* atual = this->cabeca;
            while(atual != nullptr && atual->getNumero() != numero){
                anterior = atual;
                atual = atual->getPonteiro();
            }
            if(atual != nullptr){
                if(anterior == nullptr){
                    this->cabeca = atual->getPonteiro();
                }else{
                    anterior->setPonteiro(atual->getPonteiro());
                }
                delete atual;
            }
        }
        void imprimir(){
            No* atual = this->cabeca;
            while(atual != nullptr){
                std::cout << atual->getNumero() << " ";
                atual = atual->getPonteiro();
            }
            std::cout << std::endl;
        }

};

#include <filesystem>
#include <iostream>
namespace fs = std::filesystem;

#include <string> // Add this line

#include <fstream> // Include the necessary header file for file output streams

int main() {
    #include <fstream> // Include the necessary header file for file input streams

    std::string caminho = "C:/Users/bisto/OneDrive/Documentos/GitHub/Analise-de-desempenho-UABJ-UFRPE-2024/Atividade 2/Testes/arq-novo.txt"; 
        
    //open file
    std::ifstream arquivo(caminho); // Change ofstream to ifstream for file input
    if(arquivo.is_open()){
        //processar conteudo
        std::string linha;
        L_Ligada lista;
        while(std::getline(arquivo, linha)){ // Change getline to std::getline
            std::string comando = linha.substr(0, 2);
            //std::cout << comando << std::endl;
            if (comando == "4 "){
                std::cout << linha << std::endl;
                //dividir a linha em substrings
                
            } else {
                comando = linha.substr(0, 1);

            }

        }

    }else{
        std::cout << "Erro ao abrir o arquivo" << std::endl;
    }
    return 0;
}