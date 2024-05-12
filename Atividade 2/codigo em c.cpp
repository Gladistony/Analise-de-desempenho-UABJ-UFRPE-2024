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

#include <iostream>
#include <fstream>
using namespace std;

int main() {
    // Carregar um arquivo de texo
    string myText;
    ifstream MyReadFile("Testes/arq-novo.txt");
    while (getline (MyReadFile, myText)) {
        std::cout << myText;
    }
    MyReadFile.close();
    return 0;
}