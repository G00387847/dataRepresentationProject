from BookDao import BookDao

from BookDao import BookDao

book1 = {
     'ISBN': 232345,
     'title': 'The Last Friend',
     'author': 'Frank mark',
     'price': 23

}
book2 = {
     'ISBN': 112345,
     'title': 'The Last Enemy',
     'author': 'Mac mall',
     'price': 45
}

#returnvalue = BookDao.create(book)
returnValue = BookDao.getAll()
print(returnValue)
returnValue = BookDao.findById(book2['ISBN'])
print("find By Id")
print(returnValue)
returnValue = BookDao.update(book2)
print(returnValue)
returnValue = BookDao.findById(book2['ISBN'])
print(returnValue)
returnValue = BookDao.delete(book2['ISBN'])
print(returnValue)
returnValue = BookDao.getAll()
print(returnValue)