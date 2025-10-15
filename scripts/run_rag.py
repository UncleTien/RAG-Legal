import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.rag.pipeline import query_rag

def main():
    print('🔎 RAG-Legal CLI (type exit to quit)')
    while True:
        q = input('\nQuestion> ').strip()
        if not q: 
            continue
        if q.lower() in ('exit','quit'):
            break
        ans = query_rag(q)
        print('\n--- Answer ---\n')
        print(ans)
        print('\n---------------\n')

if __name__ == '__main__':
    main()
