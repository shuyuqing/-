log = np.swapaxes(tezheng_7, 0, 1)
cax = ax.imshow(log, interpolation='nearest', origin='lower', aspect='auto')
# plt.colorbar(cax)#加上了参考的棒棒



    # plt.xticks([0, 20, 40, 60, 80, 100], ['0', '10', '20', '30', '40', '50'])
    plt.yticks([0, 5, 10, 15, 20, 25, 30, 35, 39.5], ['0', '5', '10', '15', '20', '25', '30', '35', '40'])

@@ -114,6 +118,10 @@ def mizhichuli(basedir,block,weidu):

    plt.show()

    plt.plot(log,'o')
    plt.show()



if __name__ == '__main__':
