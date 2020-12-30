from BookDao import BookDao

book1 = {
     'id': 1,
     'title': 'The Last Friend',
     'author': 'Frank mark',
     'price': 23

}
book2 = {
     'id': 2,
     'title': 'The Last Enemy',
     'author': 'Mac mall',
     'price': 40
}

# returnvalue = BookDao.create(book)
returnValue = BookDao.getAll()
print(returnValue)
returnValue = BookDao.findById(book2['id'])
print("find By Id")
print(returnValue)
returnValue = BookDao.update(book2)
print(returnValue)
returnValue = BookDao.findById(book2['id'])
print(returnValue)
returnValue = BookDao.delete(book2['id'])
print(returnValue)
returnValue = BookDao.getAll()
print(returnValue)