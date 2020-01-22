import info.index_scrap as HSI
import info.my_favorite_scrap as FAV
import info.holding_record as Hold

HSI.show_hsi()


def show_main_menu():
    print('============================================')
    print('Favorite: 1')
    print('Holding: 2')
    m_input = input()
    if m_input == '1':
        FAV.show_favorite(show_main_menu)
    elif m_input == '2':
        Hold.show_holdings(show_main_menu)


show_main_menu()
